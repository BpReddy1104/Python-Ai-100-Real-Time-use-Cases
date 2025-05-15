from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import database
from app.models.blog import Blog
from app.schemas import blog as blog_schema

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.post("/", response_model=blog_schema.Blog)
def create_blog(blog: blog_schema.BlogCreate, db: Session = Depends(database.get_db)):
    new_blog = Blog(title=blog.title, content=blog.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/", response_model=list[blog_schema.Blog])
def get_blogs(db: Session = Depends(database.get_db)):
    return db.query(Blog).all()

@router.get("/{id}", response_model=blog_schema.Blog)
def get_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.put("/{id}", response_model=blog_schema.Blog)
def update_blog(id: int, updated: blog_schema.BlogCreate, db: Session = Depends(database.get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.title = updated.title
    blog.content = updated.content
    db.commit()
    db.refresh(blog)
    return blog

@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with id {id} deleted"}
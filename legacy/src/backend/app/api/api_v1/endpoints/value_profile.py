from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.backend.app import schemas
from src.backend.app.api import deps
from src.backend.app.crud.value_profile import value_profile as crud_value_profile
from src.backend.app.models import user as models_user

router = APIRouter()

@router.post("/", response_model=schemas.ValueProfile, status_code=status.HTTP_201_CREATED)
def create_value_profile(
    *,
    db: Session = Depends(deps.get_db),
    value_profile_in: schemas.ValueProfileCreate,
    current_user: models_user.User = Depends(deps.get_current_active_user),
) -> Any:
    obj_in = value_profile_in.copy(update={"user_id": current_user.id})
    vp = crud_value_profile.create(db=db, obj_in=obj_in)
    return vp

@router.get("/", response_model=List[schemas.ValueProfile])
def read_value_profiles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user),
) -> Any:
    return crud_value_profile.get_multi_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.get("/{value_profile_id}", response_model=schemas.ValueProfile)
def read_value_profile_by_id(
    *,
    db: Session = Depends(deps.get_db),
    value_profile_id: int,
    current_user: models_user.User = Depends(deps.get_current_active_user),
) -> Any:
    vp = crud_value_profile.get(db=db, id=value_profile_id)
    if not vp or vp.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Value profile not found")
    return vp

@router.put("/{value_profile_id}", response_model=schemas.ValueProfile)
def update_value_profile(
    *,
    db: Session = Depends(deps.get_db),
    value_profile_id: int,
    value_profile_in: schemas.ValueProfileUpdate,
    current_user: models_user.User = Depends(deps.get_current_active_user),
) -> Any:
    vp = crud_value_profile.get(db=db, id=value_profile_id)
    if not vp or vp.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Value profile not found")
    vp = crud_value_profile.update(db=db, db_obj=vp, obj_in=value_profile_in)
    return vp

@router.delete("/{value_profile_id}", response_model=schemas.ValueProfile)
def delete_value_profile(
    *,
    db: Session = Depends(deps.get_db),
    value_profile_id: int,
    current_user: models_user.User = Depends(deps.get_current_active_user),
) -> Any:
    vp = crud_value_profile.get(db=db, id=value_profile_id)
    if not vp or vp.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Value profile not found")
    vp = crud_value_profile.remove(db=db, id=value_profile_id)
    return vp

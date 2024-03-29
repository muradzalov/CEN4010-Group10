import profile
from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models import Profile, CreditCard
from ..schemas import Profile as ProfileSchema
from ..schemas import Credit as CreditSchema
from sqlalchemy import insert


router = APIRouter()


#Retrieves profile using username
@router.get("/profile-management/retrieving", response_model=List[ProfileSchema])
async def find_profile(username: str, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.pusername == username)
    if not profile:
        raise HTTPException(status_code=404, detail="No profile found with specific username")
    return profile

#Creates a new profile with optional fields
@router.put("/profile-management/creating")
async def create_profile(username: str, password: str, name: Union[str, None] = None, email: Union[str, None] = None, address: Union[str, None] = None, db: Session = Depends(get_db)):
    profile_instance = Profile(
        pusername=username,
        pname=name,
        pemail=email,
        paddress=address,
        ppassword=password
    )
    db.add(profile_instance)
    db.commit()

#Updates profile with new fields
@router.put("/profile-management/updating")
async def update_profile(username: str, password: Union[str, None] = None, name: Union[str, None] = None, email: Union[str, None] = None, address: Union[str, None] = None, db: Session = Depends(get_db)):
    if password != None:
        db.query(Profile).filter(Profile.pusername == username).update({Profile.ppassword: password},
                                                                       synchronize_session=False)
        db.commit()
    if name != None:
        db.query(Profile).filter(Profile.pusername == username).update({Profile.pname: name},
                                                                       synchronize_session=False)
        db.commit()
    if email!= None:
        db.query(Profile).filter(Profile.pusername == username).update({Profile.pemail: email},
                                                                       synchronize_session=False)
        db.commit()
    if address != None:
        db.query(Profile).filter(Profile.pusername == username).update({Profile.paddress: address},
                                                                       synchronize_session=False)
        db.commit()

#Create Credit Card for User
@router.put("/profile-management/creditcard")
async def create_credit_card(username: str, creditcard: int, zipcode: int, securitycode: int, expdate: str, db: Session = Depends(get_db)):
    credit_instance = CreditCard(
        cusername = username,
        ccreditcard = creditcard,
        czipcode = zipcode,
        csc = securitycode,
        cexpdate = expdate
    )
    db.add(credit_instance)
    db.commit()
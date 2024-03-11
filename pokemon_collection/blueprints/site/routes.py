from flask import Blueprint, render_template 
from models import Pokemon


#need to instantiate our Blueprint class
site = Blueprint('site', __name__, template_folder='site_templates' )


#use site object to create our routes
@site.route('/')
def shop():
    return render_template('shop.html') #looking inside our template_folder (site_templates) to find our shop.html file

@site.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = PokeForm()
    if request.method == "POST" and form.validate_on_submit():
        poke = form.name.data
        pokemon = Pokemon()
        dict = pokemon.get_info(poke)
        pokemon.from_dict(dict)

        db.session.add(pokemon)
        db.session.commit()
       


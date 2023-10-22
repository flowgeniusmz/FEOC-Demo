def menu_navbar:
    menu_data = [
        {'icon': "far fa-copy", 'label':"Left End"},
        {'id':'Copy','icon':"🐙",'label':"Copy"},
        {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
        {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
        {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
        {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
        {'icon': "far fa-copy", 'label':"Right End"},
        {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1.1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
    ]
    
    over_theme = {'txc_inactive': '#FFFFFF'}
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        login_name='Logout',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )
import logging

def before_all(context):
    pass

def after_all(context):
    context.driver.quit()
# RegistratorBase.RegisterExtensions - метод
Выполняет регистрацию расширений. Рекомендуется не выполнять регистрацию Unity
в этом объекте.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void RegisterExtensions(
    	IExtensionContainer extensionContainer
    )
VB __Копировать
     Public Overridable Sub RegisterExtensions ( 
    	extensionContainer As IExtensionContainer
    )
C++ __Копировать
     public:
    virtual void RegisterExtensions(
    	IExtensionContainer^ extensionContainer
    )
F# __Копировать
     abstract RegisterExtensions : 
            extensionContainer : IExtensionContainer -> unit 
    override RegisterExtensions : 
            extensionContainer : IExtensionContainer -> unit 
#### Параметры
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер расширений, в котором выполняется регистрация.
#### Реализации
[IRegistrator.RegisterExtensions(IExtensionContainer)](M_Tessa_Extensions_IRegistrator_RegisterExtensions.htm)  
##  __См. также
#### Ссылки
[RegistratorBase - ](T_Tessa_Extensions_RegistratorBase.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)

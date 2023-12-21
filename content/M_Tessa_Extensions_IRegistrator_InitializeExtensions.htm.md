# IRegistrator.InitializeExtensions - метод
Выполняет инициализацию заданного контейнера расширений. Рекомендуется не
выполнять регистрацию Unity в этом объекте.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void InitializeExtensions(
    	IExtensionContainer extensionContainer
    )
VB __Копировать
     Sub InitializeExtensions ( 
    	extensionContainer As IExtensionContainer
    )
C++ __Копировать
     void InitializeExtensions(
    	IExtensionContainer^ extensionContainer
    )
F# __Копировать
     abstract InitializeExtensions : 
            extensionContainer : IExtensionContainer -> unit 
#### Параметры
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер расширений, для которого выполняется инициализация.
##  __См. также
#### Ссылки
[IRegistrator - ](T_Tessa_Extensions_IRegistrator.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)

# MessagesRegistrationHelper - класс
Вспомогательные методы регистрации команд и запросов
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class MessagesRegistrationHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class MessagesRegistrationHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class MessagesRegistrationHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type MessagesRegistrationHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MessagesRegistrationHelper
##  __Методы
[HandleWith<TCommand, THandler>(IUnityContainer,
ITypeLifetimeManager)](M_Tessa_Views_MessageServices_MessagesRegistrationHelper_HandleWith__2.htm)|
Регистрирует обработчик команды в контейнере  
---|---  
[HandleWith<TQuery, TResult, THandler>(IUnityContainer,
ITypeLifetimeManager)](M_Tessa_Views_MessageServices_MessagesRegistrationHelper_HandleWith__3.htm)|
Регистрирует обработчик запроса в контейнере  
## __См. также
#### Ссылки
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)

# ApplicationsRegistrator - класс
Осуществляет регистрацию зависимостей необходимых для работы приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ApplicationsRegistrator
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ApplicationsRegistrator
C++ __Копировать
    [ExtensionAttribute]
    public ref class ApplicationsRegistrator abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ApplicationsRegistrator = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationsRegistrator
##  __Методы
[RegisterApplicationsOnClient](M_Tessa_Applications_ApplicationsRegistrator_RegisterApplicationsOnClient.htm)|
Осуществляет регистрацию зависимостей необходимых для работы сервисов
приложений на клиентской стороне  
---|---  
[RegisterApplicationsOnServer](M_Tessa_Applications_ApplicationsRegistrator_RegisterApplicationsOnServer.htm)|
Осуществляет регистрацию зависимостей необходимых для работы сервисов
приложений на серверной стороне  
[RegisterBinder<T>](M_Tessa_Applications_ApplicationsRegistrator_RegisterBinder__1.htm)|
Регистрирует в контейнере тип объекта формируюшего пакет приложения.  
## __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)

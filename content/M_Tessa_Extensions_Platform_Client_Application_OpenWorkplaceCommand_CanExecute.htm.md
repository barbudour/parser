# OpenWorkplaceCommand.CanExecute - метод
Определяет признак доступности команды.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Application](N_Tessa_Extensions_Platform_Client_Application.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override bool CanExecute(
    	Object parameter
    )
VB __Копировать
     Public Overrides Function CanExecute ( 
    	parameter As Object
    ) As Boolean
C++ __Копировать
     public:
    virtual bool CanExecute(
    	Object^ parameter
    ) override
F# __Копировать
     abstract CanExecute : 
            parameter : Object -> bool 
    override CanExecute : 
            parameter : Object -> bool 
#### Параметры
parameter [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Параметр команды.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если команда доступна для выполнения; false в противном случае.
#### Реализации
[ICommand.CanExecute(Object)](https://learn.microsoft.com/dotnet/api/system.windows.input.icommand.canexecute#system-
windows-input-icommand-canexecute\(system-object\))  
##  __См. также
#### Ссылки
[OpenWorkplaceCommand -
](T_Tessa_Extensions_Platform_Client_Application_OpenWorkplaceCommand.htm)
[Tessa.Extensions.Platform.Client.Application - пространство
имён](N_Tessa_Extensions_Platform_Client_Application.htm)

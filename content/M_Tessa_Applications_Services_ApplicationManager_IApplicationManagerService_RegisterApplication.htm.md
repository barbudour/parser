# IApplicationManagerService.RegisterApplication - метод
Регистрация клиентского приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [OperationContractAttribute]
    void RegisterApplication(
    	int processId,
    	[NotNullAttribute] string serviceAddress
    )
VB __Копировать
    <OperationContractAttribute>
    Sub RegisterApplication ( 
    	processId As Integer,
    	<NotNullAttribute> serviceAddress As String
    )
C++ __Копировать
    [OperationContractAttribute]
    void RegisterApplication(
    	int processId, 
    	[NotNullAttribute] String^ serviceAddress
    )
F# __Копировать
     [<OperationContractAttribute>]
    abstract RegisterApplication : 
            processId : int * 
            [<NotNullAttribute>] serviceAddress : string -> unit 
#### Параметры
processId [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Идентификатор процесса приложения 
serviceAddress [String](https://learn.microsoft.com/dotnet/api/system.string)
     Адрес сервиса приложения 
## __См. также
#### Ссылки
[IApplicationManagerService -
](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)

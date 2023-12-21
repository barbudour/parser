# IApplicationManagerService.ProcessLink - метод
Производит обработку ссылок.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [OperationContractAttribute(IsOneWay = true)]
    void ProcessLink(
    	[NotNullAttribute] string link
    )
VB __Копировать
    <OperationContractAttribute(IsOneWay := true)>
    Sub ProcessLink ( 
    	<NotNullAttribute> link As String
    )
C++ __Копировать
    [OperationContractAttribute(IsOneWay = true)]
    void ProcessLink(
    	[NotNullAttribute] String^ link
    )
F# __Копировать
     [<OperationContractAttribute(IsOneWay = true)>]
    abstract ProcessLink : 
            [<NotNullAttribute>] link : string -> unit 
#### Параметры
link [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ссылка 
## __См. также
#### Ссылки
[IApplicationManagerService -
](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)

# KrProcessClientLauncherBase.PrepareParametes - метод
Обрабатывает параметры запуска процесса, которые должны быть добавлены в
дополнительную информацию используемую при запуске процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void PrepareParametes(
    	IDictionary<string, Object> requestInfo,
    	IKrProcessLauncherSpecificParameters specificParameters
    )
VB __Копировать
     Protected Overridable Sub PrepareParametes ( 
    	requestInfo As IDictionary(Of String, Object),
    	specificParameters As IKrProcessLauncherSpecificParameters
    )
C++ __Копировать
     protected:
    virtual void PrepareParametes(
    	IDictionary<String^, Object^>^ requestInfo, 
    	IKrProcessLauncherSpecificParameters^ specificParameters
    )
F# __Копировать
     abstract PrepareParametes : 
            requestInfo : IDictionary<string, Object> * 
            specificParameters : IKrProcessLauncherSpecificParameters -> unit 
    override PrepareParametes : 
            requestInfo : IDictionary<string, Object> * 
            specificParameters : IKrProcessLauncherSpecificParameters -> unit 
#### Параметры
requestInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Коллекция пар <ключ-значение> содержащая дополнительную информацию используемую при запуске процесса.
specificParameters
[IKrProcessLauncherSpecificParameters](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLauncherSpecificParameters.htm)
    Параметры запуска процесса. Параметр может иметь значение по умолчанию для типа.
##  __См. также
#### Ссылки
[KrProcessClientLauncherBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

# AddFileFromTemplateStageTypeFormatter.FormatClientAsync - метод
Выполняет форматирование ячеек на клиенте.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask FormatClientAsync(
    	IStageTypeFormatterContext context
    )
VB __Копировать
     Public Overrides Function FormatClientAsync ( 
    	context As IStageTypeFormatterContext
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask FormatClientAsync(
    	IStageTypeFormatterContext^ context
    ) override
F# __Копировать
     abstract FormatClientAsync : 
            context : IStageTypeFormatterContext -> ValueTask 
    override FormatClientAsync : 
            context : IStageTypeFormatterContext -> ValueTask 
#### Параметры
context
[IStageTypeFormatterContext](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext.htm)
    Контекст форматтера этапа.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[IStageTypeFormatter.FormatClientAsync(IStageTypeFormatterContext)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatter_FormatClientAsync.htm)  
##  __Заметки
Выполняется при открытии карточки и при каждом закрытии редактора строки. В
контексте доступны настройки этапа в виде виртуальных секций.
##  __См. также
#### Ссылки
[AddFileFromTemplateStageTypeFormatter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_AddFileFromTemplateStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)

# AddFileFromTemplateStageTypeFormatter.FormatServerAsync - метод
Выполняет форматирование ячеек на сервере.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask FormatServerAsync(
    	IStageTypeFormatterContext context
    )
VB __Копировать
     Public Overrides Function FormatServerAsync ( 
    	context As IStageTypeFormatterContext
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask FormatServerAsync(
    	IStageTypeFormatterContext^ context
    ) override
F# __Копировать
     abstract FormatServerAsync : 
            context : IStageTypeFormatterContext -> ValueTask 
    override FormatServerAsync : 
            context : IStageTypeFormatterContext -> ValueTask 
#### Параметры
context
[IStageTypeFormatterContext](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext.htm)
    Контекст форматтера этапа.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[IStageTypeFormatter.FormatServerAsync(IStageTypeFormatterContext)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatter_FormatServerAsync.htm)  
##  __Заметки
Выполняется при сохранении карточки. В контексте доступны настройки этапа в
виде хранилища ключ-значение. Серверное форматирование может быть полезно для
отображения этапов в представлениях и в легком клиенте.
##  __См. также
#### Ссылки
[AddFileFromTemplateStageTypeFormatter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_AddFileFromTemplateStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)

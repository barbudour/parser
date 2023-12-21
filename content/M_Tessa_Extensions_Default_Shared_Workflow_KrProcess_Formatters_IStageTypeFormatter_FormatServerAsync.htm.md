# IStageTypeFormatter.FormatServerAsync - метод
Выполняет форматирование ячеек на сервере.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask FormatServerAsync(
    	IStageTypeFormatterContext context
    )
VB __Копировать
     Function FormatServerAsync ( 
    	context As IStageTypeFormatterContext
    ) As ValueTask
C++ __Копировать
     ValueTask FormatServerAsync(
    	IStageTypeFormatterContext^ context
    )
F# __Копировать
     abstract FormatServerAsync : 
            context : IStageTypeFormatterContext -> ValueTask 
#### Параметры
context
[IStageTypeFormatterContext](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext.htm)
    Контекст форматтера этапа.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __Заметки
Выполняется при сохранении карточки. В контексте доступны настройки этапа в
виде хранилища ключ-значение. Серверное форматирование может быть полезно для
отображения этапов в представлениях и в легком клиенте.
##  __См. также
#### Ссылки
[IStageTypeFormatter -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)

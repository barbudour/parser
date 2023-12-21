# IStageTypeFormatterContainer.RegisterFormatter<T>(StageTypeDescriptor) -
метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     IStageTypeFormatterContainer RegisterFormatter<T>(
    	StageTypeDescriptor descriptor
    )
    where T : IStageTypeFormatter
VB __Копировать
     Function RegisterFormatter(Of T As IStageTypeFormatter) ( 
    	descriptor As StageTypeDescriptor
    ) As IStageTypeFormatterContainer
C++ __Копировать
    generic<typename T>
    where T : IStageTypeFormatter
    IStageTypeFormatterContainer^ RegisterFormatter(
    	StageTypeDescriptor^ descriptor
    )
F# __Копировать
     abstract RegisterFormatter : 
            descriptor : StageTypeDescriptor -> IStageTypeFormatterContainer  when 'T : IStageTypeFormatter
#### Параметры
descriptor
[StageTypeDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor.htm)
#### Параметры типа
T
#### Возвращаемое значение
[IStageTypeFormatterContainer](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContainer.htm)
##  __См. также
#### Ссылки
[IStageTypeFormatterContainer -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContainer.htm)
[RegisterFormatter -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContainer_RegisterFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)

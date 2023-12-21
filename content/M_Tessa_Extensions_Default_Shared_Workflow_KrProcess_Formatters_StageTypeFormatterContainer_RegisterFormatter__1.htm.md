# StageTypeFormatterContainer.RegisterFormatter<T>(StageTypeDescriptor) -
метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public IStageTypeFormatterContainer RegisterFormatter<T>(
    	StageTypeDescriptor descriptor
    )
    where T : IStageTypeFormatter
VB __Копировать
     Public Function RegisterFormatter(Of T As IStageTypeFormatter) ( 
    	descriptor As StageTypeDescriptor
    ) As IStageTypeFormatterContainer
C++ __Копировать
     public:
    generic<typename T>
    where T : IStageTypeFormatter
    virtual IStageTypeFormatterContainer^ RegisterFormatter(
    	StageTypeDescriptor^ descriptor
    ) sealed
F# __Копировать
     abstract RegisterFormatter : 
            descriptor : StageTypeDescriptor -> IStageTypeFormatterContainer  when 'T : IStageTypeFormatter
    override RegisterFormatter : 
            descriptor : StageTypeDescriptor -> IStageTypeFormatterContainer  when 'T : IStageTypeFormatter
#### Параметры
descriptor
[StageTypeDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor.htm)
#### Параметры типа
T
#### Возвращаемое значение
[IStageTypeFormatterContainer](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContainer.htm)
#### Реализации
[IStageTypeFormatterContainer.RegisterFormatter<T>(StageTypeDescriptor)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContainer_RegisterFormatter__1.htm)  
##  __См. также
#### Ссылки
[StageTypeFormatterContainer -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterContainer.htm)
[RegisterFormatter -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterContainer_RegisterFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)

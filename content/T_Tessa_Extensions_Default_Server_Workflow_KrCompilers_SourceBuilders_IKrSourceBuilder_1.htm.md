# IKrSourceBuilder<T> \- интерфейс
Описывает построитель генерируемых классов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrSourceBuilder<in T>
VB __Копировать
     Public Interface IKrSourceBuilder(Of In T)
C++ __Копировать
    generic<typename T>
    public interface class IKrSourceBuilder
F# __Копировать
     type IKrSourceBuilder<'T> = interface end
#### Параметры типа
T
    Тип объекта являющегося источником исходных кодов.
##  __Методы
[BuildSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1_BuildSources.htm)|
Выполняет компиляцию исходных кодов.  
---|---  
[FillAnchorsMap](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1_FillAnchorsMap.htm)|
Устанавливает связь между идентификатором исходного кода и объектом
идентифицирующим элемент компиляции.  
[SetClassAlias](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1_SetClassAlias.htm)|
Устанавливает алиас генерируемого класса.  
[SetClassID](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1_SetClassID.htm)|
Устанавливает идентификатор генерируемого класса.  
[SetExtraSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1_SetExtraSources.htm)|
Устанавливает дополнительные исходные коды.  
[SetLocation](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1_SetLocation.htm)|
Задаёт информацию о месте расположения текущего элемента относительно
корневого.  
[SetSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1_SetSources.htm)|
Устанавливает источник исходных кодов.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders.htm)

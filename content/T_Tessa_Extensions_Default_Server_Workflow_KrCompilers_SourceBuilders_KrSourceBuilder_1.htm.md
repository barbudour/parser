# KrSourceBuilder<T> \- класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrSourceBuilder<T> : IKrSourceBuilder<T>
VB __Копировать
     Public MustInherit Class KrSourceBuilder(Of T)
    	Implements IKrSourceBuilder(Of T)
C++ __Копировать
    generic<typename T>
    public ref class KrSourceBuilder abstract : IKrSourceBuilder<T>
F# __Копировать
     [<AbstractClassAttribute>]
    type KrSourceBuilder<'T> = 
        class
            interface IKrSourceBuilder<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrSourceBuilder<T>
Derived
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders.KrCommonMethodBuilder](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrCommonMethodBuilder.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders.KrScriptBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrScriptBuilder_1.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders.KrSingleScriptBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1.htm)
Implements
    [IKrSourceBuilder](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_IKrSourceBuilder_1.htm)<T>
#### Параметры типа
T
##  __Конструкторы
[KrSourceBuilder<T>](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1__ctor.htm)|
Инициализирует новый экземпляр класса KrSourceBuilder<T>  
---|---  
##  __Свойства
[AnchorsMap](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_AnchorsMap.htm)|  
---|---  
[ClassAlias](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_ClassAlias.htm)|  
[ClassID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_ClassID.htm)|  
[CompileSourceProvider](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_CompileSourceProvider.htm)|  
[DefaultConstructorParts](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_DefaultConstructorParts.htm)|  
[ExtraSources](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_ExtraSources.htm)|  
[Location](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_Location.htm)|  
[PreprocessorProvider](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_PreprocessorProvider.htm)|  
## __Методы
[BuildDefaultConstructor](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_BuildDefaultConstructor.htm)|  
---|---  
[BuildExtraSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_BuildExtraSources.htm)|  
[BuildSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_BuildSources.htm)|
Выполняет компиляцию исходных кодов.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FillAnchorsMap](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_FillAnchorsMap.htm)|
Устанавливает связь между идентификатором исходного кода и объектом
идентифицирующим элемент компиляции.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FormatClassName](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_FormatClassName.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetClassAlias](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetClassAlias.htm)|
Устанавливает алиас генерируемого класса.  
[SetClassID](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetClassID.htm)|
Устанавливает идентификатор генерируемого класса.  
[SetExtraSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetExtraSources.htm)|
Устанавливает дополнительные исходные коды.  
[SetLocation](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetLocation.htm)|
Задаёт информацию о месте расположения текущего элемента относительно
корневого.  
[SetSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetSources.htm)|
Устанавливает источник исходных кодов.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders.htm)

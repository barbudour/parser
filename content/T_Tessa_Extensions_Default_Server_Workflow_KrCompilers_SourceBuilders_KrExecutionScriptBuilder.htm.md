# KrExecutionScriptBuilder - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SourceBuilders](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrExecutionScriptBuilder : KrSingleScriptBuilder<IExecutionSources>
VB __Копировать
     Public NotInheritable Class KrExecutionScriptBuilder
    	Inherits KrSingleScriptBuilder(Of IExecutionSources)
C++ __Копировать
     public ref class KrExecutionScriptBuilder sealed : public KrSingleScriptBuilder<IExecutionSources^>
F# __Копировать
     [<SealedAttribute>]
    type KrExecutionScriptBuilder = 
        class
            inherit KrSingleScriptBuilder<IExecutionSources>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[KrSourceBuilder](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm)<[IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm)> __[KrSingleScriptBuilder](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1.htm)<[IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm)> __ KrExecutionScriptBuilder
##  __Конструкторы
[KrExecutionScriptBuilder](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrExecutionScriptBuilder__ctor.htm)|
Инициализирует новый экземпляр класса KrExecutionScriptBuilder  
---|---  
##  __Свойства
[AnchorsMap](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_AnchorsMap.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
---|---  
[ClassAlias](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_ClassAlias.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[ClassID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_ClassID.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[ClassPrefix](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrExecutionScriptBuilder_ClassPrefix.htm)|  
(Переопределяет
[KrSingleScriptBuilder<T>.ClassPrefix](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1_ClassPrefix.htm))  
[CompileSourceProvider](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_CompileSourceProvider.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[DefaultConstructorParts](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_DefaultConstructorParts.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[ErrorPrefix](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrExecutionScriptBuilder_ErrorPrefix.htm)|  
(Переопределяет
[KrSingleScriptBuilder<T>.ErrorPrefix](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1_ErrorPrefix.htm))  
[ExtraSources](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_ExtraSources.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[Location](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_Location.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[MethodName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrExecutionScriptBuilder_MethodName.htm)|  
(Переопределяет
[KrSingleScriptBuilder<T>.MethodName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1_MethodName.htm))  
[PreprocessorProvider](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_PreprocessorProvider.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
##  __Методы
[BuildDefaultConstructor](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_BuildDefaultConstructor.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
---|---  
[BuildExtraSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_BuildExtraSources.htm)|  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[BuildSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1_BuildSources.htm)|
Выполняет компиляцию исходных кодов.  
(Унаследован от
[KrSingleScriptBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FillAnchorsMap](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_FillAnchorsMap.htm)|
Устанавливает связь между идентификатором исходного кода и объектом
идентифицирующим элемент компиляции.  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FormatClassName](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1_FormatClassName.htm)|  
(Унаследован от
[KrSingleScriptBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1.htm))  
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
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[SetClassID](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetClassID.htm)|
Устанавливает идентификатор генерируемого класса.  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[SetExtraSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetExtraSources.htm)|
Устанавливает дополнительные исходные коды.  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[SetLocation](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetLocation.htm)|
Задаёт информацию о месте расположения текущего элемента относительно
корневого.  
(Унаследован от
[KrSourceBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1.htm))  
[SetSources](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrExecutionScriptBuilder_SetSources.htm)|
Устанавливает источник исходных кодов.  
(Переопределяет
[KrSourceBuilder<T>.SetSources(T)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSourceBuilder_1_SetSources.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[SourceText](F_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1_SourceText.htm)|  
(Унаследован от
[KrSingleScriptBuilder<T>](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SourceBuilders_KrSingleScriptBuilder_1.htm))  
---|---  
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

# MergeTree<T, TMergeOptions> \- класс
##  __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class MergeTree<T, TMergeOptions> : IMergeTree<T, TMergeOptions>
    where TMergeOptions : IMergeOptions
VB __Копировать
     Public Class MergeTree(Of T, TMergeOptions As IMergeOptions)
    	Implements IMergeTree(Of T, TMergeOptions)
C++ __Копировать
    generic<typename T, typename TMergeOptions>
    where TMergeOptions : IMergeOptions
    public ref class MergeTree : IMergeTree<T, TMergeOptions>
F# __Копировать
     type MergeTree<'T, 'TMergeOptions when 'TMergeOptions : IMergeOptions> = 
        class
            interface IMergeTree<'T, 'TMergeOptions>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MergeTree<T, TMergeOptions>
Implements
    [IMergeTree](T_Tessa_SmartMerge_IMergeTree_2.htm)<T, TMergeOptions>
#### Параметры типа
T
TMergeOptions
##  __Конструкторы
[MergeTree<T, TMergeOptions>](M_Tessa_SmartMerge_MergeTree_2__ctor.htm)|
Инициализирует новый экземпляр класса MergeTree<T, TMergeOptions>  
---|---  
##  __Свойства
[Tiers](P_Tessa_SmartMerge_MergeTree_2_Tiers.htm)|  
---|---  
## __Методы
[CalculateDeletedAndUpdated](M_Tessa_SmartMerge_MergeTree_2_CalculateDeletedAndUpdated.htm)|  
---|---  
[CalculateInserted](M_Tessa_SmartMerge_MergeTree_2_CalculateInserted.htm)|  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Merge](M_Tessa_SmartMerge_MergeTree_2_Merge.htm)|  
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
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)

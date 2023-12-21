# CardMergeResultItemBase - класс
Базовый MergeResultItem для Card
## __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.MergeResultItems](N_Tessa_Cards_SmartMerge_MergeResultItems.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardMergeResultItemBase : IMergeResultItem<Card>
VB __Копировать
     Public MustInherit Class CardMergeResultItemBase
    	Implements IMergeResultItem(Of Card)
C++ __Копировать
     public ref class CardMergeResultItemBase abstract : IMergeResultItem<Card^>
F# __Копировать
     [<AbstractClassAttribute>]
    type CardMergeResultItemBase = 
        class
            interface IMergeResultItem<Card>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMergeResultItemBase
Derived
[Tessa.Cards.SmartMerge.MergeResultItems.CardSectionMergeResultItemBase](T_Tessa_Cards_SmartMerge_MergeResultItems_CardSectionMergeResultItemBase.htm)
[Tessa.Cards.SmartMerge.MergeResultItems.Files.FileMergeResultItemBase](T_Tessa_Cards_SmartMerge_MergeResultItems_Files_FileMergeResultItemBase.htm)
[Tessa.Cards.SmartMerge.MergeResultItems.TaskHistory.TaskHistoryMergeResultItemBase](T_Tessa_Cards_SmartMerge_MergeResultItems_TaskHistory_TaskHistoryMergeResultItemBase.htm)
[Tessa.Cards.SmartMerge.MergeResultItems.TaskHistoryGroups.TaskHistoryGroupsMergeResultItemBase](T_Tessa_Cards_SmartMerge_MergeResultItems_TaskHistoryGroups_TaskHistoryGroupsMergeResultItemBase.htm)
[Tessa.Cards.SmartMerge.MergeResultItems.Tasks.TaskMergeResultItemBase](T_Tessa_Cards_SmartMerge_MergeResultItems_Tasks_TaskMergeResultItemBase.htm)
Implements
    [IMergeResultItem](T_Tessa_SmartMerge_IMergeResultItem_1.htm)<[Card](T_Tessa_Cards_Card.htm)>
##  __Конструкторы
[CardMergeResultItemBase](M_Tessa_Cards_SmartMerge_MergeResultItems_CardMergeResultItemBase__ctor.htm)|
Инициализирует новый экземпляр класса CardMergeResultItemBase  
---|---  
##  __Методы
[ApplyAsync](M_Tessa_Cards_SmartMerge_MergeResultItems_CardMergeResultItemBase_ApplyAsync.htm)|
Применяет результат слияния к объекту.  
---|---  
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
[GetChildren<TValue,
TIdentifier>](M_Tessa_Cards_SmartMerge_MergeResultItems_CardMergeResultItemBase_GetChildren__2.htm)|
Находит дочерние элементы для определенного элемента в lookUp, где ключем
являются родительские идентификаторы  
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
[Tessa.Cards.SmartMerge.MergeResultItems - пространство
имён](N_Tessa_Cards_SmartMerge_MergeResultItems.htm)

# SchemeSubmittingQueue - класс
##  __Definition
 **Пространство имён:**
[Tessa.Scheme.Differences](N_Tessa_Scheme_Differences.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SchemeSubmittingQueue : SubmittingQueue<SchemeObject, SchemeSubmittingQueueItem>
VB __Копировать
     Public NotInheritable Class SchemeSubmittingQueue
    	Inherits SubmittingQueue(Of SchemeObject, SchemeSubmittingQueueItem)
C++ __Копировать
     public ref class SchemeSubmittingQueue sealed : public SubmittingQueue<SchemeObject^, SchemeSubmittingQueueItem^>
F# __Копировать
     [<SealedAttribute>]
    type SchemeSubmittingQueue = 
        class
            inherit SubmittingQueue<SchemeObject, SchemeSubmittingQueueItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm) __[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue_2.htm)<[SchemeObject](T_Tessa_Scheme_SchemeObject.htm), [SchemeSubmittingQueueItem](T_Tessa_Scheme_Differences_SchemeSubmittingQueueItem.htm)> __ SchemeSubmittingQueue
##  __Конструкторы
[SchemeSubmittingQueue](M_Tessa_Scheme_Differences_SchemeSubmittingQueue__ctor.htm)|
Инициализирует новый экземпляр класса SchemeSubmittingQueue  
---|---  
##  __Свойства
[Builder](P_Tessa_Scheme_Differences_SchemeSubmittingQueue_Builder.htm)|  
---|---  
[Count](P_Tessa_Platform_Differences_SubmittingQueue_Count.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[Database](P_Tessa_Scheme_Differences_SchemeSubmittingQueue_Database.htm)|  
[Exception](P_Tessa_Platform_Differences_SubmittingQueue_Exception.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[FaultedItem](P_Tessa_Platform_Differences_SubmittingQueue_FaultedItem.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[Item](P_Tessa_Platform_Differences_SubmittingQueue_2_Item.htm)|  
(Унаследован от [SubmittingQueue<TObject,
TItem>](T_Tessa_Platform_Differences_SubmittingQueue_2.htm))  
[Service](P_Tessa_Scheme_Differences_SchemeSubmittingQueue_Service.htm)|  
[State](P_Tessa_Platform_Differences_SubmittingQueue_State.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
##  __Методы
[AddItem](M_Tessa_Platform_Differences_SubmittingQueue_AddItem.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
---|---  
[Contains(TItem)](M_Tessa_Platform_Differences_SubmittingQueue_2_Contains.htm)|  
(Унаследован от [SubmittingQueue<TObject,
TItem>](T_Tessa_Platform_Differences_SubmittingQueue_2.htm))  
[Contains(SubmittingQueueItem)](M_Tessa_Platform_Differences_SubmittingQueue_Contains.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[CopyTo(TItem[],
Int32)](M_Tessa_Platform_Differences_SubmittingQueue_2_CopyTo.htm)|  
(Унаследован от [SubmittingQueue<TObject,
TItem>](T_Tessa_Platform_Differences_SubmittingQueue_2.htm))  
[CopyTo(SubmittingQueueItem[],
Int32)](M_Tessa_Platform_Differences_SubmittingQueue_CopyTo.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
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
[GetEnumerator](M_Tessa_Platform_Differences_SubmittingQueue_2_GetEnumerator.htm)|  
(Унаследован от [SubmittingQueue<TObject,
TItem>](T_Tessa_Platform_Differences_SubmittingQueue_2.htm))  
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
[IndexOf(TItem)](M_Tessa_Platform_Differences_SubmittingQueue_2_IndexOf.htm)|  
(Унаследован от [SubmittingQueue<TObject,
TItem>](T_Tessa_Platform_Differences_SubmittingQueue_2.htm))  
[IndexOf(SubmittingQueueItem)](M_Tessa_Platform_Differences_SubmittingQueue_IndexOf.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RefreshAsync](M_Tessa_Platform_Differences_SubmittingQueue_RefreshAsync.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[RefreshCoreAsync](M_Tessa_Scheme_Differences_SchemeSubmittingQueue_RefreshCoreAsync.htm)|  
(Переопределяет
[SubmittingQueue.RefreshCoreAsync(CancellationToken)](M_Tessa_Platform_Differences_SubmittingQueue_RefreshCoreAsync.htm))  
[SetFaultedItem](M_Tessa_Platform_Differences_SubmittingQueue_SetFaultedItem.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[SubmitAddedItemAsync](M_Tessa_Scheme_Differences_SchemeSubmittingQueue_SubmitAddedItemAsync.htm)|  
(Переопределяет [SubmittingQueue<TObject, TItem>.SubmitAddedItemAsync(TObject,
CancellationToken)](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitAddedItemAsync.htm))  
[SubmitAsync](M_Tessa_Platform_Differences_SubmittingQueue_SubmitAsync.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[SubmitCoreAsync](M_Tessa_Scheme_Differences_SchemeSubmittingQueue_SubmitCoreAsync.htm)|  
(Переопределяет
[SubmittingQueue.SubmitCoreAsync(CancellationToken)](M_Tessa_Platform_Differences_SubmittingQueue_SubmitCoreAsync.htm))  
[SubmitItemAsync](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitItemAsync.htm)|  
(Унаследован от [SubmittingQueue<TObject,
TItem>](T_Tessa_Platform_Differences_SubmittingQueue_2.htm))  
[SubmitModifiedItemAsync](M_Tessa_Scheme_Differences_SchemeSubmittingQueue_SubmitModifiedItemAsync.htm)|  
(Переопределяет [SubmittingQueue<TObject,
TItem>.SubmitModifiedItemAsync(TObject,
CancellationToken)](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitModifiedItemAsync.htm))  
[SubmitRemovedItemAsync](M_Tessa_Scheme_Differences_SchemeSubmittingQueue_SubmitRemovedItemAsync.htm)|  
(Переопределяет [SubmittingQueue<TObject,
TItem>.SubmitRemovedItemAsync(TObject,
CancellationToken)](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitRemovedItemAsync.htm))  
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
[Tessa.Scheme.Differences - пространство имён](N_Tessa_Scheme_Differences.htm)

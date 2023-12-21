# CardRowStateEventArgs - класс
Аргументы события, происходящего при изменении свойства
[State](P_Tessa_Cards_CardRow_State.htm) в объекте с информацией о строке
коллекционной или древовидной секции в пакете карточки
[CardRow](T_Tessa_Cards_CardRow.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardRowStateEventArgs : CardStateEventArgs<CardRowState>
VB __Копировать
     Public NotInheritable Class CardRowStateEventArgs
    	Inherits CardStateEventArgs(Of CardRowState)
C++ __Копировать
     public ref class CardRowStateEventArgs sealed : public CardStateEventArgs<CardRowState>
F# __Копировать
     [<SealedAttribute>]
    type CardRowStateEventArgs = 
        class
            inherit CardStateEventArgs<CardRowState>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __[CardStateEventArgs](T_Tessa_Cards_CardStateEventArgs_1.htm)<[CardRowState](T_Tessa_Cards_CardRowState.htm)> __ CardRowStateEventArgs
##  __Конструкторы
[CardRowStateEventArgs](M_Tessa_Cards_CardRowStateEventArgs__ctor.htm)|
Создаёт экземпляр класса с указанием предыдущего и текущего состояния строки
коллекционной или древовидной секции.  
---|---  
## __Свойства
[NewState](P_Tessa_Cards_CardStateEventArgs_1_NewState.htm)|  Текущее
состояние.  
(Унаследован от
[CardStateEventArgs<TState>](T_Tessa_Cards_CardStateEventArgs_1.htm))  
---|---  
[OldState](P_Tessa_Cards_CardStateEventArgs_1_OldState.htm)|  Предыдущее
состояние.  
(Унаследован от
[CardStateEventArgs<TState>](T_Tessa_Cards_CardStateEventArgs_1.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

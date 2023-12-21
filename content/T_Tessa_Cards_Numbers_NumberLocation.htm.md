# NumberLocation - класс
Информация по местоположению номера в карточке или в контексте события,
происходящего с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NumberLocation : INumberLocation, 
    	ISealable
VB __Копировать
     Public Class NumberLocation
    	Implements INumberLocation, ISealable
C++ __Копировать
     public ref class NumberLocation : INumberLocation, 
    	ISealable
F# __Копировать
     type NumberLocation = 
        class
            interface INumberLocation
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberLocation
Derived
[Tessa.Cards.Numbers.CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm)
Implements
    [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[NumberLocation](M_Tessa_Cards_Numbers_NumberLocation__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Info](P_Tessa_Cards_Numbers_NumberLocation_Info.htm)| Дополнительная
информация, связанная с местоположением номера.  
---|---  
[IsSealed](P_Tessa_Cards_Numbers_NumberLocation_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
[Manager](P_Tessa_Cards_Numbers_NumberLocation_Manager.htm)| Объект,
определяющий поведение текущего объекта.  
[Type](P_Tessa_Cards_Numbers_NumberLocation_Type.htm)| Тип расположения номера
(в карточке или в контексте события, происходящего с номером).  
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
[Seal](M_Tessa_Cards_Numbers_NumberLocation_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Cards_Numbers_NumberLocation_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](M_Tessa_Cards_Numbers_NumberLocation_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
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
[StoreNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreNumberAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[ToCardNumberLocation](M_Tessa_Cards_Numbers_NumberExtensions_ToCardNumberLocation.htm)|
Преобразует местоположение номера
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm) типа
[Card](F_Tessa_Cards_Numbers_NumberLocationTypes_Card.htm) в объект
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm). Может
вернуть null, если преобразование не удалось.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

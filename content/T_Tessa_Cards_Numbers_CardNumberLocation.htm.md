# CardNumberLocation - класс
Информация о местоположении полей с номерами в карточке, а именно о названиях
секций и полей, в которых расположены номера.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardNumberLocation : NumberLocation
VB __Копировать
     Public NotInheritable Class CardNumberLocation
    	Inherits NumberLocation
C++ __Копировать
     public ref class CardNumberLocation sealed : public NumberLocation
F# __Копировать
     [<SealedAttribute>]
    type CardNumberLocation = 
        class
            inherit NumberLocation
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm) __ CardNumberLocation
##  __Конструкторы
[CardNumberLocation](M_Tessa_Cards_Numbers_CardNumberLocation__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств. Сразу после
создания класс считается защищённым от изменений.  
---|---  
## __Свойства
[FullNumberField](P_Tessa_Cards_Numbers_CardNumberLocation_FullNumberField.htm)|
Имя поля со строковым представлением номера.  
---|---  
[Info](P_Tessa_Cards_Numbers_NumberLocation_Info.htm)| Дополнительная
информация, связанная с местоположением номера.  
(Унаследован от [NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm))  
[IsSealed](P_Tessa_Cards_Numbers_NumberLocation_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от [NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm))  
[Manager](P_Tessa_Cards_Numbers_NumberLocation_Manager.htm)| Объект,
определяющий поведение текущего объекта.  
(Унаследован от [NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm))  
[NumberField](P_Tessa_Cards_Numbers_CardNumberLocation_NumberField.htm)|  Имя
поля с числовым представлением номера.  
[Section](P_Tessa_Cards_Numbers_CardNumberLocation_Section.htm)|  Имя секции,
содержащей поля с номером.  
[SequenceNameField](P_Tessa_Cards_Numbers_CardNumberLocation_SequenceNameField.htm)|
Имя поля с названием последовательности, из которой был выделен номер.  
[Type](P_Tessa_Cards_Numbers_NumberLocation_Type.htm)| Тип расположения номера
(в карточке или в контексте события, происходящего с номером).  
(Унаследован от [NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm))  
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
(Унаследован от [NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm))  
[SealInternal](M_Tessa_Cards_Numbers_NumberLocation_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от [NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm))  
[ToString](M_Tessa_Cards_Numbers_CardNumberLocation_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[NumberLocation.ToString()](M_Tessa_Cards_Numbers_NumberLocation_ToString.htm))  
[TryCreate](M_Tessa_Cards_Numbers_CardNumberLocation_TryCreate.htm)|  Создаёт
объект CardNumberLocation по данным из хеш-таблицы info. Возвращает null, если
хеш-таблица не содержит всех необходимых данных.  
## __Методы расширения
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
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

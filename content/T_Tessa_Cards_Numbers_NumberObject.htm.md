# NumberObject - класс
Объект, определяющий свойства номера и средства его хранения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NumberObject : INumberObject, 
    	IComparable<INumberObject>, IEquatable<INumberObject>, ISealable
VB __Копировать
     Public Class NumberObject
    	Implements INumberObject, IComparable(Of INumberObject), 
    	IEquatable(Of INumberObject), ISealable
C++ __Копировать
     public ref class NumberObject : INumberObject, 
    	IComparable<INumberObject^>, IEquatable<INumberObject^>, ISealable
F# __Копировать
     type NumberObject = 
        class
            interface INumberObject
            interface IComparable<INumberObject>
            interface IEquatable<INumberObject>
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberObject
Implements
    [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>, [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Заметки
При сравнении номеров посредством
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\)) не учитывается тип номера. При сравнении номеров
посредством
[CompareTo(T)](https://learn.microsoft.com/dotnet/api/system.icomparable-1.compareto#system-
icomparable-1-compareto\(-0\)) учитывается только порядковый номер. Наследники
класса могут определить дополнительные свойства номера. Эти свойства и тип
сравниваемого объекта не учитываются в методе сравнения для реализации
[IEquatable<T>](https://learn.microsoft.com/dotnet/api/system.iequatable-1).
## __Конструкторы
[NumberObject](M_Tessa_Cards_Numbers_NumberObject__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств и функций, определяющих его
поведение.  
---|---  
## __Свойства
[FullNumber](P_Tessa_Cards_Numbers_NumberObject_FullNumber.htm)|  Строковое
представление номера или null, если номер не задан.  
---|---  
[Info](P_Tessa_Cards_Numbers_NumberObject_Info.htm)| Дополнительная
информация, связанная с местоположением номера.  
[IsSealed](P_Tessa_Cards_Numbers_NumberObject_IsSealed.htm)| Признак того, что
объект был защищён от изменений.  
[Manager](P_Tessa_Cards_Numbers_NumberObject_Manager.htm)| Объект,
определяющий поведение текущего объекта.  
[Number](P_Tessa_Cards_Numbers_NumberObject_Number.htm)|  Числовое
представление номера или null, если номер не задан.  
[SequenceName](P_Tessa_Cards_Numbers_NumberObject_SequenceName.htm)|  Название
последовательности, из которой взят номер, или null, если номер не задан или
не взят из последовательности.  
[Type](P_Tessa_Cards_Numbers_NumberObject_Type.htm)|  Тип номера. Может быть
взят из полей класса [Tessa.Cards.Numbers.NumberTypes].  
## __Методы
[CompareTo](M_Tessa_Cards_Numbers_NumberObject_CompareTo.htm)| Выполняет
сравнение текущего объекта с заданным.  
---|---  
[CreateEmpty](M_Tessa_Cards_Numbers_NumberObject_CreateEmpty.htm)|  Создаёт
объект NumberObject, описывающий пустой номер.  
[Equals(INumberObject)](M_Tessa_Cards_Numbers_NumberObject_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Cards_Numbers_NumberObject_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_Numbers_NumberObject_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsEmpty](M_Tessa_Cards_Numbers_NumberObject_IsEmpty.htm)|  Возвращает признак
того, что объект [Tessa.Cards.Numbers.INumberObject] представляет из себя
ссылку на отсутствующий (или ещё не известный) номер. Как правило, номер
считается пустым, если его строка полного номера равна null или пустой строке,
а также либо отсутствует числовой номер, либо имя последовательности равно
null или пустой строке. Т.о. пустой номер не является номером из
последовательности.  
[IsSequential()](M_Tessa_Cards_Numbers_NumberObject_IsSequential.htm)|
Возвращает признак того, что объект [Tessa.Cards.Numbers.INumberObject]
представляет из себя ссылку на номер из последовательности. Как правило, номер
считается взятым из последовательности, если его числовое представление, и имя
последовательности не равны null или пустой строке. Строка полного номера
может быть равна null или пустой строке. Т.о. пустой номер не является номером
из последовательности. Если номер не является номером из последовательности,
то его нельзя освободить, дерезервировать или выделить повторно.  
[IsSequential(Nullable<Int64>,
String)](M_Tessa_Cards_Numbers_NumberObject_IsSequential_1.htm)|  Возвращает
признак того, что номер, содержащий указанные значения в полях, является
номером из последовательности.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Cards_Numbers_NumberObject_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Cards_Numbers_NumberObject_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](M_Tessa_Cards_Numbers_NumberObject_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[RefreshFullNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_RefreshFullNumberAsync.htm)|
Обновляет поле с полным номером
[FullNumber](P_Tessa_Cards_Numbers_INumberObject_FullNumber.htm) для заданного
номера, если номер является номером последовательности, и возвращает объект
номера с такими же данными, но другим полным номером, или возвращает тот же
номер, если он не является номером последовательности.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[StoreAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync_2.htm)|
Сохраняет объект с номером в заданном контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[StoreAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[StoreAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync_1.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

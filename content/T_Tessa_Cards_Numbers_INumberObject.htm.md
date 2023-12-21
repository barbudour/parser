# INumberObject - интерфейс
Объект, определяющий свойства номера и средства его хранения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberObject : IComparable<INumberObject>, 
    	IEquatable<INumberObject>, ISealable
VB __Копировать
     Public Interface INumberObject
    	Inherits IComparable(Of INumberObject), IEquatable(Of INumberObject), 
    	ISealable
C++ __Копировать
     public interface class INumberObject : IComparable<INumberObject^>, 
    	IEquatable<INumberObject^>, ISealable
F# __Копировать
     type INumberObject = 
        interface
            interface IComparable<INumberObject>
            interface IEquatable<INumberObject>
            interface ISealable
        end
Implements
    [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<INumberObject>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<INumberObject>, [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Заметки
При сравнении номеров посредством
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\)) не учитывается тип номера. При сравнении номеров
посредством
[CompareTo(T)](https://learn.microsoft.com/dotnet/api/system.icomparable-1.compareto#system-
icomparable-1-compareto\(-0\)) учитывается только порядковый номер.
## __Свойства
[FullNumber](P_Tessa_Cards_Numbers_INumberObject_FullNumber.htm)|  Строковое
представление номера или null, если номер не задан.  
---|---  
[Info](P_Tessa_Cards_Numbers_INumberObject_Info.htm)| Дополнительная
информация, связанная с номером.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Manager](P_Tessa_Cards_Numbers_INumberObject_Manager.htm)| Объект,
определяющий поведение текущего объекта.  
[Number](P_Tessa_Cards_Numbers_INumberObject_Number.htm)|  Числовое
представление номера или null, если номер не задан.  
[SequenceName](P_Tessa_Cards_Numbers_INumberObject_SequenceName.htm)|
Название последовательности, из которой взят номер, или null, если номер не
задан или не взят из последовательности.  
[Type](P_Tessa_Cards_Numbers_INumberObject_Type.htm)|  Тип номера. Может быть
взят из полей класса [Tessa.Cards.Numbers.NumberTypes].  
## __Методы
[CompareTo](https://learn.microsoft.com/dotnet/api/system.icomparable-1.compareto#system-
icomparable-1-compareto\(-0\))| Compares the current instance with another
object of the same type and returns an integer that indicates whether the
current instance precedes, follows, or occurs in the same position in the sort
order as the other object.  
(Унаследован от
[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<INumberObject>)  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<INumberObject>)  
[IsEmpty](M_Tessa_Cards_Numbers_INumberObject_IsEmpty.htm)|  Возвращает
признак того, что объект [Tessa.Cards.Numbers.INumberObject] представляет из
себя ссылку на отсутствующий (или ещё не известный) номер. Как правило, номер
считается пустым, если его строка полного номера равна null или пустой строке,
а также либо отсутствует числовой номер, либо имя последовательности равно
null или пустой строке. Т.о. пустой номер не является номером из
последовательности.  
[IsSequential](M_Tessa_Cards_Numbers_INumberObject_IsSequential.htm)|
Возвращает признак того, что объект [Tessa.Cards.Numbers.INumberObject]
представляет из себя ссылку на номер из последовательности. Как правило, номер
считается взятым из последовательности, если его числовое представление, и имя
последовательности не равны null или пустой строке. Строка полного номера
может быть равна null или пустой строке. Т.о. пустой номер не является номером
из последовательности. Если номер не является номером из последовательности,
то его нельзя освободить, дерезервировать или выделить повторно.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __Методы расширения
[RefreshFullNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_RefreshFullNumberAsync.htm)|
Обновляет поле с полным номером
[FullNumber](P_Tessa_Cards_Numbers_INumberObject_FullNumber.htm) для заданного
номера, если номер является номером последовательности, и возвращает объект
номера с такими же данными, но другим полным номером, или возвращает тот же
номер, если он не является номером последовательности.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
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

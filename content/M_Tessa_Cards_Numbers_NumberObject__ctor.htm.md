# NumberObject - конструктор
Создаёт экземпляр класса с указанием значений его свойств и функций,
определяющих его поведение.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberObject(
    	long? number,
    	string fullNumber,
    	string sequenceName,
    	NumberTypeDescriptor type,
    	INumberObjectManager manager
    )
VB __Копировать
     Public Sub New ( 
    	number As Long?,
    	fullNumber As String,
    	sequenceName As String,
    	type As NumberTypeDescriptor,
    	manager As INumberObjectManager
    )
C++ __Копировать
     public:
    NumberObject(
    	Nullable<long long> number, 
    	String^ fullNumber, 
    	String^ sequenceName, 
    	NumberTypeDescriptor^ type, 
    	INumberObjectManager^ manager
    )
F# __Копировать
     new : 
            number : Nullable<int64> * 
            fullNumber : string * 
            sequenceName : string * 
            type : NumberTypeDescriptor * 
            manager : INumberObjectManager -> NumberObject
#### Параметры
number
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
    Числовое представление номера или null, если номер не задан.
fullNumber [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строковое представление номера или null, если номер не задан.
sequenceName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Название последовательности, из которой взят номер, или null, если номер не задан или не взят из последовательности. 
type [NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
     Тип номера. Может быть взят из полей класса [NumberTypes](T_Tessa_Cards_Numbers_NumberTypes.htm). Не может быть равен null. 
manager [INumberObjectManager](T_Tessa_Cards_Numbers_INumberObjectManager.htm)
     Объект, определяющий поведение создаваемого объекта. Не может быть равен null. 
## __См. также
#### Ссылки
[NumberObject - ](T_Tessa_Cards_Numbers_NumberObject.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

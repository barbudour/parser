# NumberObject.CreateEmpty - метод
Создаёт объект [NumberObject](T_Tessa_Cards_Numbers_NumberObject.htm),
описывающий пустой номер.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static NumberObject CreateEmpty(
    	NumberTypeDescriptor numberType,
    	INumberObjectManager manager
    )
VB __Копировать
     Public Shared Function CreateEmpty ( 
    	numberType As NumberTypeDescriptor,
    	manager As INumberObjectManager
    ) As NumberObject
C++ __Копировать
     public:
    static NumberObject^ CreateEmpty(
    	NumberTypeDescriptor^ numberType, 
    	INumberObjectManager^ manager
    )
F# __Копировать
     static member CreateEmpty : 
            numberType : NumberTypeDescriptor * 
            manager : INumberObjectManager -> NumberObject 
#### Параметры
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера. Не может быть равен null.
manager [INumberObjectManager](T_Tessa_Cards_Numbers_INumberObjectManager.htm)
     Объект, определяющий методы создаваемого объекта. Не может быть равен null. 
#### Возвращаемое значение
[NumberObject](T_Tessa_Cards_Numbers_NumberObject.htm)  
Созданный объект.
##  __См. также
#### Ссылки
[NumberObject - ](T_Tessa_Cards_Numbers_NumberObject.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

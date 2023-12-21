# CardTypeControl.Create - метод
Создаёт экземпляр класса, унаследованного от
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm) и описываемого кодом
typeCode.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardTypeControl Create(
    	byte typeCode
    )
VB __Копировать
     Public Shared Function Create ( 
    	typeCode As Byte
    ) As CardTypeControl
C++ __Копировать
     public:
    static CardTypeControl^ Create(
    	unsigned char typeCode
    )
F# __Копировать
     static member Create : 
            typeCode : byte -> CardTypeControl 
#### Параметры
typeCode [Byte](https://learn.microsoft.com/dotnet/api/system.byte)
     Код, которым описывается тип создаваемого объекта. Он может быть получен методом [GetTypeCode(Type)](M_Tessa_Cards_CardTypeControl_GetTypeCode.htm). 
#### Возвращаемое значение
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)  
Экземпляр класса, имеющий тип, определяемый заданным кодом typeCode.
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

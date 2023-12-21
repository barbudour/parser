# CardTypeControl.GetTypeCode - метод
Возвращает код, при помощи которого можно определить тип класса,
унаследованного от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static byte GetTypeCode(
    	Type type
    )
VB __Копировать
     Public Shared Function GetTypeCode ( 
    	type As Type
    ) As Byte
C++ __Копировать
     public:
    static unsigned char GetTypeCode(
    	Type^ type
    )
F# __Копировать
     static member GetTypeCode : 
            type : Type -> byte 
#### Параметры
type [Type](https://learn.microsoft.com/dotnet/api/system.type)
    Тип класса, унаследованного от [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm).
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)  
Код, при помощи которого можно определить заданный тип класса.
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

# CardComponentHelper.GetStoreMode - метод
Возвращает способ сохранения карточки по её версии.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardStoreMode GetStoreMode(
    	int cardVersion
    )
VB __Копировать
     Public Shared Function GetStoreMode ( 
    	cardVersion As Integer
    ) As CardStoreMode
C++ __Копировать
     public:
    static CardStoreMode GetStoreMode(
    	int cardVersion
    )
F# __Копировать
     static member GetStoreMode : 
            cardVersion : int -> CardStoreMode 
#### Параметры
cardVersion [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Версия сохраняемой карточки.
#### Возвращаемое значение
[CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)  
Способ сохранения карточки с заданной версией.
##  __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

# ICardStoreCachingStrategy.TryGetRowRemover - метод
Возвращает из кэша объект, выполняющий удаление строк из заданной
коллекционной или древовидной секции, или null, если объект не найден в кэше.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     CardSectionRowRemover TryGetRowRemover(
    	Guid sectionID
    )
VB __Копировать
     Function TryGetRowRemover ( 
    	sectionID As Guid
    ) As CardSectionRowRemover
C++ __Копировать
    CardSectionRowRemover^ TryGetRowRemover(
    	Guid sectionID
    )
F# __Копировать
     abstract TryGetRowRemover : 
            sectionID : Guid -> CardSectionRowRemover 
#### Параметры
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор коллекционной или древовидной секции, из которой требуется удалять строки.
#### Возвращаемое значение
[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)  
Объект, выполняющий удаление строк из заданной коллекционной или древовидной
секции, или null, если объект не найден в кэше.
## __См. также
#### Ссылки
[ICardStoreCachingStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

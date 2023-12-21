# CardHelper.HasFilesContentsToSave - метод
Возвращает признак того, что в заданной карточке присутствует хотя бы один
файл, который был добавлен или содержимое которого было изменено.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasFilesContentsToSave(
    	Card card
    )
VB __Копировать
     Public Shared Function HasFilesContentsToSave ( 
    	card As Card
    ) As Boolean
C++ __Копировать
     public:
    static bool HasFilesContentsToSave(
    	Card^ card
    )
F# __Копировать
     static member HasFilesContentsToSave : 
            card : Card -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой выполняется проверка. Не равна null.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в заданной карточке присутствует хотя бы один файл, который был
добавлен или содержимое которого было изменено; false в противном случае.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

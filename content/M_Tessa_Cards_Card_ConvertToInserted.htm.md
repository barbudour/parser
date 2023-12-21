# Card.ConvertToInserted - метод
Изменяет карточку таким образом, что все её строки, файлы и задания считаются
добавленными, т.е. имеют состояние [Inserted](T_Tessa_Cards_CardRowState.htm)
или [Inserted](T_Tessa_Cards_CardFileState.htm), а также для карточки указан
[StoreMode](P_Tessa_Cards_Card_StoreMode.htm) как
[Insert](T_Tessa_Cards_CardStoreMode.htm). Возвращает признак того, что в
карточке были сделаны изменения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool ConvertToInserted()
VB __Копировать
     Public Function ConvertToInserted As Boolean
C++ __Копировать
     public:
    bool ConvertToInserted()
F# __Копировать
     member ConvertToInserted : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в карточке были сделаны изменения; false, если карточка осталась
неизменной.
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

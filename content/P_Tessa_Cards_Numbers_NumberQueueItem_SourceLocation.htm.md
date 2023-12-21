# NumberQueueItem.SourceLocation - свойство
Информация по местоположению номера в карточке, по которому номер следует
прочитать для выполнения действия. Если местоположение указано, то номер
[Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm) и тип номера
[SourceNumberType](P_Tessa_Cards_Numbers_NumberQueueItem_SourceNumberType.htm)
игнорируются.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberStorageLocation SourceLocation { get; set; }
VB __Копировать
     Public Property SourceLocation As NumberStorageLocation
    	Get
    	Set
C++ __Копировать
     public:
    property NumberStorageLocation^ SourceLocation {
    	NumberStorageLocation^ get ();
    	void set (NumberStorageLocation^ value);
    }
F# __Копировать
     member SourceLocation : NumberStorageLocation with get, set
#### Значение свойства
[NumberStorageLocation](T_Tessa_Cards_Numbers_NumberStorageLocation.htm)
##  __Заметки
По умолчанию указывается тип
[Type](P_Tessa_Cards_Numbers_NumberStorageLocation_Type.htm), равный
[NotAssigned](F_Tessa_Cards_Numbers_NumberLocationTypes_NotAssigned.htm), что
определяет использование номера из свойства
[Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm) для выполнения
действия.
## __См. также
#### Ссылки
[NumberQueueItem - ](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

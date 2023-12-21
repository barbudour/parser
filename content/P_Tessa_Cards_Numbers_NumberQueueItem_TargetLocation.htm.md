# NumberQueueItem.TargetLocation - свойство
Информация по местоположению номера в карточке, по которому номер следует
сохранить после выполнения действия.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberStorageLocation TargetLocation { get; set; }
VB __Копировать
     Public Property TargetLocation As NumberStorageLocation
    	Get
    	Set
C++ __Копировать
     public:
    property NumberStorageLocation^ TargetLocation {
    	NumberStorageLocation^ get ();
    	void set (NumberStorageLocation^ value);
    }
F# __Копировать
     member TargetLocation : NumberStorageLocation with get, set
#### Значение свойства
[NumberStorageLocation](T_Tessa_Cards_Numbers_NumberStorageLocation.htm)
##  __Заметки
По умолчанию указывается тип
[Type](P_Tessa_Cards_Numbers_NumberStorageLocation_Type.htm), равный
[NotAssigned](F_Tessa_Cards_Numbers_NumberLocationTypes_NotAssigned.htm), что
определяет отсутствие каких-либо действий с номером после выполнения текущего
действия.
## __См. также
#### Ссылки
[NumberQueueItem - ](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

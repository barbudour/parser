# NumberQueueItem.SourceNumberType - свойство
Тип номера с дополнительной информацией, по которому номер следует прочитать
для выполнения действия, или null, если тип не указан и номер следует получить
из свойства [Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm). Если
тип номера указан, то номер
[Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm) игнорируется, но
при этом свойство
[SourceLocation](P_Tessa_Cards_Numbers_NumberQueueItem_SourceLocation.htm)
должно быть равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberStorageTypeDescriptor SourceNumberType { get; set; }
VB __Копировать
     Public Property SourceNumberType As NumberStorageTypeDescriptor
    	Get
    	Set
C++ __Копировать
     public:
    property NumberStorageTypeDescriptor^ SourceNumberType {
    	NumberStorageTypeDescriptor^ get ();
    	void set (NumberStorageTypeDescriptor^ value);
    }
F# __Копировать
     member SourceNumberType : NumberStorageTypeDescriptor with get, set
#### Значение свойства
[NumberStorageTypeDescriptor](T_Tessa_Cards_Numbers_NumberStorageTypeDescriptor.htm)
##  __См. также
#### Ссылки
[NumberQueueItem - ](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

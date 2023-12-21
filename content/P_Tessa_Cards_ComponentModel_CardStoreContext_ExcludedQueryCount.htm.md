# CardStoreContext.ExcludedQueryCount - свойство
Количество запросов, выполненных через
[Executor](P_Tessa_Cards_ComponentModel_CardStoreContext_Executor.htm),
которые не учитываются в стандартном API при определении того, следует ли
выполнять проверку и инкремент версии карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int ExcludedQueryCount { get; set; }
VB __Копировать
     Public Property ExcludedQueryCount As Integer
    	Get
    	Set
C++ __Копировать
     public:
    property int ExcludedQueryCount {
    	int get ();
    	void set (int value);
    }
F# __Копировать
     member ExcludedQueryCount : int with get, set
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __Заметки
Свойство используется, например, для подсчёта количества запросов при создании
файлов, чтобы добавляемые файлы при изменении карточки могли не увеличивать
версию.
## __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

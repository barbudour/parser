# CardTypeEntryControl.DisplayFormat - свойство
Формат отображаемого в текстовом виде поля.
Если задано null или пустая строка, то в текстовом виде поле будет
отображаться как значения всех колонок из списка
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeEntryControl_PhysicalColumnIDList.htm),
объединённые пробелами.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string DisplayFormat { get; set; }
VB __Копировать
     Public Property DisplayFormat As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ DisplayFormat {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member DisplayFormat : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Пример значения: {0} ({1})
Это означает, что сначала будет выведено текстовое значение первой колонки из
списка
[PhysicalColumnIDList](P_Tessa_Cards_CardTypeEntryControl_PhysicalColumnIDList.htm),
а затем в круглых скобках второе значение.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeEntryControl - ](T_Tessa_Cards_CardTypeEntryControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]

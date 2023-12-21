# CardTypeControl.BlockSettings - свойство
Настройки блока [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm), которые
задаются для каждого включённого в его состав объекта.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject BlockSettings { get; set; }
VB __Копировать
     Public Property BlockSettings As ISerializableObject
    	Get
    	Set
C++ __Копировать
     public:
    property ISerializableObject^ BlockSettings {
    	ISerializableObject^ get ();
    	void set (ISerializableObject^ value);
    }
F# __Копировать
     member BlockSettings : ISerializableObject with get, set
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __Заметки
Такие настройки удобно использовать для указания местоположения элемента в
блоке, если блок предоставляет особый способ расположения, такой как Grid
(таблица с несколькими строками и столбцами; в настройках каждого вложенного в
блок объекта указываются номера его строки и столбца).
Объект сериализуется в BSON, который размещается в base-64 строке во вложенном
XML-элементе.
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]

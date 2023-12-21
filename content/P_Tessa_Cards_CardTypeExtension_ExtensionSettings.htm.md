# CardTypeExtension.ExtensionSettings - свойство
Дополнительные настройки расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject ExtensionSettings { get; set; }
VB __Копировать
     Public Property ExtensionSettings As ISerializableObject
    	Get
    	Set
C++ __Копировать
     public:
    property ISerializableObject^ ExtensionSettings {
    	ISerializableObject^ get ();
    	void set (ISerializableObject^ value);
    }
F# __Копировать
     member ExtensionSettings : ISerializableObject with get, set
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __Заметки
Объект сериализуется в BSON, который размещается в base-64 строке во вложенном
XML-элементе.
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeExtension - ](T_Tessa_Cards_CardTypeExtension.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]

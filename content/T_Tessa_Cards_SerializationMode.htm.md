# SerializationMode - перечисление
Способ десериализации, указываемый в методах
[!:CardSerializableObject.OnDeserializingAsync] и
[!:CardSerializableObject.OnDeserializedAsync].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum SerializationMode
VB __Копировать
     Public Enumeration SerializationMode
C++ __Копировать
     public enum class SerializationMode
F# __Копировать
     type SerializationMode
##  __Заметки
Методы не вызываются для бинарной десериализации.
## __Члены
Xml| 0|  Десериализация из xml.  
---|---|---  
Storage| 1|  Десериализация из хранилища Dictionary<string, object>.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

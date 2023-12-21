# CardSerializableObject.SerializeToJson - метод
Сериализует объект и его дочерние объекты в форме текстового JSON с
сохраняемыми типами данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string SerializeToJson(
    	bool indented = false
    )
VB __Копировать
     Public Function SerializeToJson ( 
    	Optional indented As Boolean = false
    ) As String
C++ __Копировать
     public:
    String^ SerializeToJson(
    	bool indented = false
    )
F# __Копировать
     member SerializeToJson : 
            ?indented : bool 
    (* Defaults:
            let _indented = defaultArg indented false
    *)
    -> string 
#### Параметры
indented [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что в выводимом тексте должны быть отступы (табуляции) и переводы строк.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Сериализованный JSON.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

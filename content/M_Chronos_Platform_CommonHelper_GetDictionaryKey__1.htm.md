# CommonHelper.GetDictionaryKey<T> \- метод
Возвращает уникальный ключ для использования в хеш-таблицах вида
IDictionary{string,object}.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetDictionaryKey<T>(
    	string name
    )
VB __Копировать
     Public Shared Function GetDictionaryKey(Of T) ( 
    	name As String
    ) As String
C++ __Копировать
     public:
    generic<typename T>
    static String^ GetDictionaryKey(
    	String^ name
    )
F# __Копировать
     static member GetDictionaryKey : 
            name : string -> string 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя свойства, уникальное в рамках типа.
#### Параметры типа
T
    Тип, использующий свойство.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строка, являющаяся уникальным ключом.
##  __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)

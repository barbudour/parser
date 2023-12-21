# LocalFileEntry.GetKey - метод
Возвращает значение используемое в качестве ключа в
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string GetKey(
    	Func<LocalFileEntry, string> predicate = null
    )
VB __Копировать
     Public Function GetKey ( 
    	Optional predicate As Func(Of LocalFileEntry, String) = Nothing
    ) As String
C++ __Копировать
     public:
    String^ GetKey(
    	Func<LocalFileEntry^, String^>^ predicate = nullptr
    )
F# __Копировать
     member GetKey : 
            ?predicate : Func<LocalFileEntry, string> 
    (* Defaults:
            let _predicate = defaultArg predicate null
    *)
    -> string 
#### Параметры
predicate
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[LocalFileEntry](T_Tessa_Applications_Synchronization_LocalFileEntry.htm),
[String](https://learn.microsoft.com/dotnet/api/system.string)> (Optional)
    Функция вычисляющая значение ключа, если оно не было задано при инициализации объекта.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Значение используемое в качестве ключа в
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm).
##  __См. также
#### Ссылки
[LocalFileEntry - ](T_Tessa_Applications_Synchronization_LocalFileEntry.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)

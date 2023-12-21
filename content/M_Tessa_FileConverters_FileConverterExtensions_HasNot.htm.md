# FileConverterExtensions.HasNot - метод
Возвращает признак того, что заданный флаг не установлен.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasNot(
    	this FileConverterRequestFlags flags,
    	FileConverterRequestFlags flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function HasNot ( 
    	flags As FileConverterRequestFlags,
    	flag As FileConverterRequestFlags
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool HasNot(
    	FileConverterRequestFlags flags, 
    	FileConverterRequestFlags flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member HasNot : 
            flags : FileConverterRequestFlags * 
            flag : FileConverterRequestFlags -> bool 
#### Параметры
flags
[FileConverterRequestFlags](T_Tessa_FileConverters_FileConverterRequestFlags.htm)
    Установленные флаги.
flag
[FileConverterRequestFlags](T_Tessa_FileConverters_FileConverterRequestFlags.htm)
     Флаг, который требуется проверить. Если указано несколько флагов, то проверяется, что нет ни одного установленного флага. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что заданный флаг не установлен.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[FileConverterRequestFlags](T_Tessa_FileConverters_FileConverterRequestFlags.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[FileConverterExtensions -
](T_Tessa_FileConverters_FileConverterExtensions.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)

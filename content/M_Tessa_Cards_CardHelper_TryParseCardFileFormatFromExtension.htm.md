# CardHelper.TryParseCardFileFormatFromExtension - метод
Определяет формат файла по расширению. Возвращает null, если определить формат
не удалось.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardFileFormat? TryParseCardFileFormatFromExtension(
    	string extension
    )
VB __Копировать
     Public Shared Function TryParseCardFileFormatFromExtension ( 
    	extension As String
    ) As CardFileFormat?
C++ __Копировать
     public:
    static Nullable<CardFileFormat> TryParseCardFileFormatFromExtension(
    	String^ extension
    )
F# __Копировать
     static member TryParseCardFileFormatFromExtension : 
            extension : string -> Nullable<CardFileFormat> 
#### Параметры
extension [String](https://learn.microsoft.com/dotnet/api/system.string)
     Расширение файла, по которому определяется формат. Должно начинаться с ведущей точки. Может быть равно null. 
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[CardFileFormat](T_Tessa_Cards_CardFileFormat.htm)>  
Формат файла, определённый по его расширению, или null, если определить формат
не удалось.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

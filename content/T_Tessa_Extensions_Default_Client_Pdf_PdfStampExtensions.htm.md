# PdfStampExtensions - класс
Вспомогательные методы-расширения для пространства имён
Tessa.Extensions.Platform.Client.Models.PdfStamps.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Pdf](N_Tessa_Extensions_Default_Client_Pdf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PdfStampExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class PdfStampExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class PdfStampExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type PdfStampExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PdfStampExtensions
##  __Методы
[AppendDate](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions_AppendDate.htm)|
Добавляет строку с заданной датой в штамп. Дата не конвертируется в локальное
время и выводится как есть.  
---|---  
[RegisterPdfStampExtensionTypes](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions_RegisterPdfStampExtensionTypes.htm)|  
[WhenPdfStampFunc](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions_WhenPdfStampFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IPdfStampExtension](T_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Pdf - пространство
имён](N_Tessa_Extensions_Default_Client_Pdf.htm)

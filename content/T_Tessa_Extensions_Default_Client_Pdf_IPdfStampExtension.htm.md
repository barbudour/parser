# IPdfStampExtension - интерфейс
Расширение для простановки штампов в документах PDF на клиенте.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Pdf](N_Tessa_Extensions_Default_Client_Pdf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPdfStampExtension : IExtension
VB __Копировать
     Public Interface IPdfStampExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IPdfStampExtension : IExtension
F# __Копировать
     type IPdfStampExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[GenerateForPage](M_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtension_GenerateForPage.htm)|
Выполняется генерации для каждой обрабатываемой страницы.  
---|---  
[OnGenerationEnded](M_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtension_OnGenerationEnded.htm)|
Выполняется при окончании генерации после обработки всех страниц.  
[OnGenerationStarted](M_Tessa_Extensions_Default_Client_Pdf_IPdfStampExtension_OnGenerationStarted.htm)|
Выполняется при начале генерации перед обработкой страниц.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Pdf - пространство
имён](N_Tessa_Extensions_Default_Client_Pdf.htm)

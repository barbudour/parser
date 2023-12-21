# Tessa.Views.Parser - пространство имён
Парсер метаинформации представлений.
##  __Классы
[DefaultViewGetDataExecutor](T_Tessa_Views_Parser_DefaultViewGetDataExecutor.htm)|  
---|---  
[IndentationStrategy](T_Tessa_Views_Parser_IndentationStrategy.htm)|
Стратегия выравнивания символов  
[LexemeParser](T_Tessa_Views_Parser_LexemeParser.htm)|  Осуществляет парсинг
переданного текста. Исходный текст имеет следующий формат.
#keyword[([Param1[:Value], [ParamN[:Value]])] [{] [}] [{] [}] В качестве
экранирующего символа используется \. Парсинг осуществляет передачей в метод
[Parse(String, Int32)](M_Tessa_Views_Parser_LexemeParser_Parse.htm) исходного
текста На выходе парсер выдает коллекцию элементов кода
[CodeBlockCollection](T_Tessa_Views_Parser_ExpressionEval_CodeBlockCollection.htm)
В случае ошибки разбора текста генерирует исключения
[ParserException](T_Tessa_Views_Parser_ParserException.htm) Возможные
состояния: ProcessText - Находится в режиме обработки текста и поиска начала
ключевого слова ProcessKeyword - Находится в режиме обработки имени ключевого
слова ProcessOpenedBracket - Находится в режиме поиска - '('
ProcessOpenedCurveBracket - Находится в режиме поиска - '{'
ProcessClosingBracket - Находится в режиме поиска закрывающейся ')'
ProcessClosingCurveBracket - Находится в режиме поиска закрывающейся '}'
Возможные переходы между состояниями: ProcessText -> ProcessKeyword
ProcessKeyword -> ProcessText -> ProcessOpenedBracket -> ProcessComment
ProcessOpenedBracket -> ProcessOpendedCurveBracket -> ProcessClosingBracket
ProcessOpendedCurveBracket -> ProcessClosingCurveBracket -> ProcessText
ProcessClosingBracket -> ProcessText -> ProcessOpenedCurveBracket ->
ProcessComment ProcessClosingCurveBracket -> ProcessOpenedCurveBracket  
[ParameterBuilder](T_Tessa_Views_Parser_ParameterBuilder.htm)|  Построитель
списка параметров  
[ParametersDictionary](T_Tessa_Views_Parser_ParametersDictionary.htm)|
Коллекция ключ-значения предназначенная для хранения списка параметров.  
[ParserException](T_Tessa_Views_Parser_ParserException.htm)|  Исключение
вызываемое при ошибке разбора выражений  
[ParserNames](T_Tessa_Views_Parser_ParserNames.htm)|  Вспомогательные
процедуры  
[SyntaxConverterOptions](T_Tessa_Views_Parser_SyntaxConverterOptions.htm)|
Опции конвертации лексем в синтаксическое дерево  
[TessaParserHelper](T_Tessa_Views_Parser_TessaParserHelper.htm)|
Вспомогательные методы для парсинга текстов шаблонизатора  
[TessaViewModelAdapter](T_Tessa_Views_Parser_TessaViewModelAdapter.htm)|
Адаптирует модель представления
[TessaViewModel](T_Tessa_Views_TessaViewModel.htm) в
[представление.](T_Tessa_Views_ITessaView.htm)  
[TextBuilder](T_Tessa_Views_Parser_TextBuilder.htm)|  Осуществляет построение
текстов  
[UnknownKeywordException](T_Tessa_Views_Parser_UnknownKeywordException.htm)|
Исключение вызываемое при ошибке  
## __Интерфейсы
[IIndentationStrategy](T_Tessa_Views_Parser_IIndentationStrategy.htm)|
Описание интерфейса стратегии выравнивание текста  
---|---  
[IKeywordNodeTypesRegistry<TKeywordNode>](T_Tessa_Views_Parser_IKeywordNodeTypesRegistry_1.htm)|
Описание интерфейса реестра узлов парсера  
[IParameterBuilder](T_Tessa_Views_Parser_IParameterBuilder.htm)|  Описание
интерфейса для объектов осуществляющих построение списка параметров ключевых
слов  
[ITextBuilder](T_Tessa_Views_Parser_ITextBuilder.htm)|  Построитель текстов
файлов  
[IViewGetDataExecutor](T_Tessa_Views_Parser_IViewGetDataExecutor.htm)|
Описание интерфейса исполнителя функции получения данных от представления  
## __Перечисления
[BraceLayout](T_Tessa_Views_Parser_BraceLayout.htm)|  Местоположение фигурных
скобок  
---|---
